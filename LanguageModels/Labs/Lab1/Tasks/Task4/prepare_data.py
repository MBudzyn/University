import re
import random

class PrepareData:
    def __init__(self, test_ratio=0.2, seed=random.randint(0, 10000)):
        self.test_ratio = test_ratio
        random.seed(seed)

        self.question_data_path = "../../lecture_materials/txt/task4_questions.txt"
        self.answers_data_path = "../../lecture_materials/txt/task4_answers.txt"
        self.full_data = self.build_full_data()
        self.groups = self.prepare_data()
        self.splits = self.split_train_test()
        self.execute()

    def build_full_data(self):
        with open(self.question_data_path, "r", encoding="utf-8") as fq, \
             open(self.answers_data_path, "r", encoding="utf-8") as fa:
            return [{"Q": q.strip(), "A": a.strip()} for q, a in zip(fq, fa)]

    def get_case(self, item):
        q = item["Q"].lower().strip()
        if re.match(r'^czy\b', q) and q.count("czy") == 1:
            return 0
        elif q.startswith(("ile", "ilu")):
            return 1
        elif (" czy " in q and not q.startswith("czy")) or q.count("czy") >= 2 \
                or re.search(r'[:,]\s*[^:]*\s*czy\s', q):
            return 2
        q_words = q.split()
        if len(q_words) >= 3 and q_words[0] in ["w", "z"] and q_words[1] in ["której", "którego", "którym", "których"]:
            return 3
        if len(q_words) >= 3 and q_words[0] in ["jak", "kto", "co", "jakiej", "który", "która", "którego", "której"]:
            return 4
        return 5

    def assign_to_group(self, item, case, groups):
        if case == 0:
            groups["tak_nie_data"].append(item)
        elif case == 1:
            groups["number_answer_data"].append(item)
        elif case == 2:
            groups["part_of_question_data"].append(item)
        elif case == 3:
            groups["prep_key_data"].append(item)
        elif case == 4:
            groups["first_words_data"].append(item)
        else:
            groups["other_data"].append(item)

    def prepare_data(self):
        groups = {
            "tak_nie_data": [],
            "number_answer_data": [],
            "part_of_question_data": [],
            "prep_key_data": [],
            "first_words_data": [],
            "other_data": []
        }

        for item in self.full_data:
            self.assign_to_group(item=item, case=self.get_case(item), groups=groups)

        return groups

    def split_train_test(self):
        splits = {}
        for name, items in self.groups.items():
            if not items:
                splits[name] = {"train": [], "test": []}
                continue

            if name == "tak_nie_data":
                yes = [x for x in items if x["A"].lower() == "tak"]
                no = [x for x in items if x["A"].lower() == "nie"]

                def stratified_split(subset):
                    random.shuffle(subset)
                    test_size = max(1, int(len(subset) * self.test_ratio))
                    return subset[test_size:], subset[:test_size]

                yes_train, yes_test = stratified_split(yes)
                no_train, no_test = stratified_split(no)

                train = yes_train + no_train
                test = yes_test + no_test
                random.shuffle(train)
                random.shuffle(test)
            else:
                random.shuffle(items)
                test_size = max(1, int(len(items) * self.test_ratio))
                test = items[:test_size]
                train = items[test_size:]

            splits[name] = {"train": train, "test": test}

        return splits

    def build_few_shot_prompt(self, group_name: str, question: str, n: int = 10, is_test: bool = False) -> str:
        data = self.get_group_data(group_name, is_test=is_test)
        if not data:
            raise ValueError(f"Brak danych w grupie '{group_name}' dla {'test' if is_test else 'train'}.")
        examples = random.sample(data, min(n, len(data)))

        prompt = ""
        for ex in examples:
            q, a = ex["Q"].strip(), ex["A"].strip()
            prompt += f"Pytanie: {q}\nOdpowiedź: {a}\n\n"

        prompt += f"Pytanie: {question.strip()}\nOdpowiedź:"
        return prompt.strip()

    def get_group_data(self, group_name, is_test=False):
        if group_name not in self.splits:
            raise ValueError(f"Nieznana grupa: {group_name}")
        split_type = "test" if is_test else "train"
        return self.splits[group_name][split_type]

    def get_all_train_data(self):
        return [item for g in self.splits.values() for item in g["train"]]

    def get_all_test_data(self):
        return [item for g in self.splits.values() for item in g["test"]]

    def print_data(self):
        for name, values in self.groups.items():
            print(f"{name}: {len(values)} elementów")

    def print_splits(self):
        for name, split in self.splits.items():
            print(f"\n{name}:")
            print(f"  Train: {len(split['train'])}")
            print(f"  Test:  {len(split['test'])}")

    def execute(self):
        self.print_data()
        self.print_splits()


if __name__ == "__main__":
    prep = PrepareData()