from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    #A is a knight or a knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    #if A is a knight then the statement is true
    Implication(AKnight, And(AKnight, AKnave)),
    #if A is a knave then the statement is false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #A and B are knights or knaves but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    #if A is a knight then A and B are both knaves
    Implication(AKnight, And(AKnave, BKnave)),
    #if A is a knave then the statement is false
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    #A and B are knights or knaves but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    #if A is a knight then A and B are both the same
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    #if A is a knave then the statement is false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight then A and B are not the same
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave then the statement is false
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #A, B and C are knights or knaves but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    #if B is a knight then A said 'I am a knave', and C is a knave
    Implication(BKnight, CKnave),
    Implication(BKnight, And(
        #A then said 'I am a Knave' then A may be a Knight or a Knave
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave)),
    )),
    #if B is a knave then A said 'I am a knight' C is not a knave
    Implication(BKnave, Not(CKnave)),
    Implication(BKnave, And(
        #A then said 'I am a Knight' then A may be a Knight or a Knave
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnight))
    )),
    #if C is a knight then A is a knight
    Implication(CKnight, AKnight),
    #if C is a knave then A is not a knight
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
