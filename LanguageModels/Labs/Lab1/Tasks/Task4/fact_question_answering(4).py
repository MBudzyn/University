from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from prepare_data import PrepareData
import random
from answer_check_for_task4 import evaluate_answers

class FactQuestionAnswering:
    def __init__(self, model_name='eryk-mazus/polka-1.1b', device='cpu'):
        self.data_preparator = PrepareData()
        self.model_name = model_name
        self.device = device
        self.tokenizer = None
        self.model = None
        self.load_model()

    def load_model(self):
        print(f"Loading model {self.model_name} on {self.device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)
        print("Model loaded successfully.")

    def answer_yes_no(self, question, n_examples=8):
        if n_examples % 2 != 0:
            n_examples += 1

        yes_items = [x for x in self.data_preparator.get_group_data("tak_nie_data") if x["A"].lower() == "tak"]
        no_items = [x for x in self.data_preparator.get_group_data("tak_nie_data") if x["A"].lower() == "nie"]

        n_each = n_examples // 2
        if len(yes_items) < n_each or len(no_items) < n_each:
            raise ValueError("Za mało danych do zbudowania równoważnego few-shot promptu.")

        yes_sample = random.sample(yes_items, n_each)
        no_sample = random.sample(no_items, n_each)
        examples = yes_sample + no_sample
        random.shuffle(examples)

        prompt = "Poniżej przykłady pytań i jednoznacznych odpowiedzi 'tak' lub 'nie'. Odpowiedz jednym słowem.\n\n"
        for ex in examples:
            prompt += f"Pytanie: {ex['Q'].strip()}\nOdpowiedź: {ex['A'].strip()}\n\n"
        prompt += f"Pytanie: {question.strip()}\nOdpowiedź:"

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                max_length=input_ids.shape[1] + 5,
                pad_token_id=self.tokenizer.eos_token_id,
                attention_mask=(input_ids != self.tokenizer.pad_token_id),
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )

        answer = self.tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True).strip().lower()
        if answer.startswith("tak"):
            return "tak"
        elif answer.startswith("nie"):
            return "nie"
        else:
            return random.choice(["tak", "nie"])

    def answer_number_case(self, question):
        prompt = self.data_preparator.build_few_shot_prompt("number_answer_data", question, n=5)
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                attention_mask=(input_ids != self.tokenizer.pad_token_id),
                pad_token_id=self.tokenizer.eos_token_id,
                max_length=input_ids.shape[1] + 5
            )
        answer = self.tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True).strip()
        return answer

    def answer_part_of_question(self, question):
        words = question.split()
        words = words[2:]

        if words:
            words[-1] = words[-1].rstrip("?")

        czy_ind = words.index("czy") if "czy" in words else 0

        vectors_left = [-4, -3, -2, -1]
        candidates = []

        for v_ind in range(len(vectors_left) - 1):
            candidates.append(words[vectors_left[v_ind] + czy_ind])
            candidates.append(words[vectors_left[v_ind] + czy_ind] + " " + words[vectors_left[v_ind + 1] + czy_ind])
        candidates.append(words[vectors_left[-1] + czy_ind])

        if czy_ind + 1 < len(words):
            candidates.append(words[czy_ind + 1])
        if czy_ind + 2 < len(words):
            candidates.append(words[czy_ind + 2])
            candidates.append(words[czy_ind + 1] + " " + words[czy_ind + 2])

        scores = {}
        for c in candidates:
            prompt = f"{question.strip()}\nOdpowiedź: {c}"
            input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
            with torch.no_grad():
                loss = self.model(input_ids, labels=input_ids).loss.item()
            scores[c] = -loss

        best = max(scores, key=scores.get)
        return best

    def answer_prep_key_case(self, question):
        prompt = self.data_preparator.build_few_shot_prompt("prep_key_data", question, n=5)
        prompt += "\nOdpowiedź:"

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)

        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                attention_mask=(input_ids != self.tokenizer.pad_token_id),
                pad_token_id=self.tokenizer.pad_token_id if self.tokenizer.pad_token_id is not None else self.tokenizer.eos_token_id,
                max_length=input_ids.shape[1] + 100,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                top_k=50,
                num_return_sequences=1
            )

        generated_tokens = output_ids[0][input_ids.shape[1]:]

        if generated_tokens.nelement() == 0:
            return "(brak wygenerowanej odpowiedzi)"

        answer = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        if not answer:
            return "(brak wygenerowanej odpowiedzi)"

        return answer.strip()

    def answer_first_words_case(self, question):

        prompt = self.data_preparator.build_few_shot_prompt("first_words_data", question, n=5)
        prompt += "\nOdpowiedź:"

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)

        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                attention_mask=(input_ids != self.tokenizer.pad_token_id),
                pad_token_id=self.tokenizer.pad_token_id if self.tokenizer.pad_token_id is not None else self.tokenizer.eos_token_id,
                max_length=input_ids.shape[1] + 50,  # dajemy więcej miejsca na generację
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                top_k=50,
                num_return_sequences=1
            )

        generated_tokens = output_ids[0][input_ids.shape[1]:]

        if generated_tokens.nelement() == 0:
            return "(brak wygenerowanej odpowiedzi)"

        answer = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        if not answer:
            return "(brak wygenerowanej odpowiedzi)"

        return answer.strip()
    def answer_other_case(self, question):
        prompt = self.data_preparator.build_few_shot_prompt("other_data", question, n=5)
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                max_length=input_ids.shape[1] + 20,
                pad_token_id=self.tokenizer.eos_token_id,
                attention_mask=(input_ids != self.tokenizer.pad_token_id),
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )
        answer = self.tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True).strip()
        return answer

    def handler(self, record):
        question = record["Q"]
        case_type = self.data_preparator.get_case(record)

        if case_type == 0:
            return self.answer_yes_no(question)
        elif case_type == 1:
            return self.answer_number_case(question)
        elif case_type == 2:
            return self.answer_part_of_question(question)
        elif case_type == 3:
            return self.answer_prep_key_case(question)
        elif case_type == 4:
            return self.answer_first_words_case(question)
        elif case_type == 5:
            return self.answer_other_case(question)
        else:
            return None

    def process_questions(self):
        answers_file = "answers_all.txt"
        correct_file = "correct_answers_all.txt"

        with open(answers_file, "w", encoding="utf-8") as af, \
                open(correct_file, "w", encoding="utf-8") as caf:

            for group_name in ["other_data"]:
                group = self.data_preparator.get_group_data(group_name, is_test=True)
                if not group:
                    continue

                print(f"🧩 Przetwarzanie grupy TEST: {group_name} (liczba pytań: {len(group)})")

                found_answers_group = []
                correct_answers_group = []

                for i, record in enumerate(group):
                    question = record["Q"]
                    correct = record["A"]
                    print(f"   ▶️ Pytanie {i + 1}/{len(group)}: {question}")

                    try:
                        answer = self.handler(record)
                        af.write(answer.strip() + "\n")
                        caf.write(correct.strip() + "\n")

                        answer_lower = answer.strip().lower()
                        correct_lower = correct.strip().lower().split("\t")

                        found_answers_group.append(answer_lower)
                        correct_answers_group.append(correct_lower)

                        print(f"      ✅ Odpowiedź: {answer.strip()}")
                        print(f"      ✅ Poprawna odpowiedź: {correct.strip()}")
                    except Exception as e:
                        print(f"⚠️ Błąd przy pytaniu: {question}\n   {e}")
                        af.write("ERROR\n")
                        caf.write(correct.strip() + "\n")

                        found_answers_group.append("ERROR")
                        correct_answers_group.append(correct.strip().lower().split("\t"))

                results_group, score_group = evaluate_answers(found_answers_group, correct_answers_group)
                print(f"📊 Wynik dla grupy '{group_name}': {score_group:.2f}%")

        with open(answers_file, encoding="utf-8") as af, open(correct_file, encoding="utf-8") as caf:
            found_answers_all = [x.strip().lower() for x in af]
            correct_answers_all = [x.strip().lower().split("\t") for x in caf]

        results_all, overall_score = evaluate_answers(found_answers_all, correct_answers_all)
        print(f"\n🌐 TOTAL OVERALL SCORE dla całego datasetu: {overall_score:.2f}%")


if __name__ == "__main__":
    fq = FactQuestionAnswering()
    fq.process_questions()
