import editdistance

def scaled_editdist(ans, cor):
    ans = ans.lower()
    cor = cor.lower()
    return editdistance.eval(ans, cor) / len(cor)

def single_match(a, c):
    if c.isdecimal():
        return a == c
    return scaled_editdist(a, c) < 0.5

def match(ans, cor):
    # cor jest listą możliwych poprawnych odpowiedzi
    return any(single_match(ans, c) for c in cor)

def evaluate_answers(found_answers, correct_answers):
    """
    Zwraca szczegółowe wyniki porównania oraz ogólny wynik procentowy.
    found_answers: lista stringów z odpowiedziami modelu
    correct_answers: lista list stringów z poprawnymi odpowiedziami
    """
    results = []
    score = 0.0
    records = len(correct_answers)

    for idx, (ans, cor) in enumerate(zip(found_answers, correct_answers), start=1):
        is_correct = match(ans, cor)
        results.append({
            "index": idx,
            "found": ans,
            "correct": cor,
            "is_correct": is_correct
        })
        if is_correct:
            score += 1

    overall_score = score / records * 100 if records else 0.0
    return results, overall_score

found_answers = [x.strip().lower() for x in open('../../Tasks/Task4/answers.txt', encoding='utf-8')]
correct_answers = [x.strip().lower().split('\t') for x in open('../../Tasks/Task4/correct_answers.txt', encoding='utf-8')]

results, overall_score = evaluate_answers(found_answers, correct_answers)

print(f"TOTAL SCORE: {overall_score:.2f}%")