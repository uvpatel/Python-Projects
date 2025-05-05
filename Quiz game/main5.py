# Quiz Game in Python with three levels

# Beginner level questions
questions = [  # 1
    ["Who created Python language?", "Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling", 2],
    # 2
    ["Who created C language?", "Brad Luis", "Dennis Ritchie", "Alan Turing", "Ken Thompson", 2],
    # 3
    ["Who created C++ language?", "Ada Lovelace", "Linus Torvalds", "Dennis Ritchie", "Bjarne Stroustrup", 4],
    # 4
    ["Who created Java language?", "Brendan Eich", "James Gosling", "Grace Hopper", "Barbara Liskov", 2],
    # 5
    ["Who created JavaScript language?", "Larry Wall", "Steve Wozniak", "Tim Berners-Lee", "Brendan Eich", 4],
    # 6
    ["Who created Ruby language?", "Håkon Wium Lie", "Linus Torvalds", "Yukihiro Matsumoto", "John McCarthy", 3],
    # 7
    ["Who created PHP language?", "Mark Zuckerberg", "James Gosling", "Rasmus Lerdorf", "Guido van Rossum", 3],
    # 8
    ["Who created Swift language?", "Chris Lattner", "Brad Cox", "Tim Berners-Lee", "Anders Hejlsberg", 1],
    # 9
    ["Who created Go (Golang) language?", "Robert Griesemer, Rob Pike, and Ken Thompson", "Brian Kernighan", "James Gosling", "John Backus", 1],
    # 10
    ["Who created Rust language?", "Graydon Hoare", "Bill Gates", "Guido van Rossum", "Brendan Eich", 1],
    # 11
    ["Who created TypeScript language?", "Anders Hejlsberg", "Elon Musk", "Dennis Ritchie", "Grace Hopper", 1],
    # 12
    ["Who created Kotlin language?", "Margaret Hamilton", "Bjarne Stroustrup", "James Gosling", "JetBrains", 4],
    # 13
    ["Who created Perl language?", "Larry Wall", "Linus Torvalds", "Vint Cerf", "Dennis Ritchie", 1],
    # 14
    ["Who created MATLAB language?", "Cleve Moler", "Ada Lovelace", "Brian Kernighan", "Ken Thompson", 1],
    # 15
    ["Who created R language?", "Robert Gentleman and Ross Ihaka", "Herbert Simon", "Alan Turing", "Claude Shannon", 1],
    # 16
    ["Who created Scala language?", "Bill Gates", "Martin Odersky", "Brendan Eich", "Dennis Ritchie", 2],
    # 17
    ["Who created Dart language?", "Ken Thompson", "Robert Griesemer", "Bjarne Stroustrup", "Google", 4],
    # 18
    ["Who created Erlang language?", "Joe Armstrong", "Guido van Rossum", "Linus Torvalds", "Dennis Ritchie", 1],
    # 19
    ["Who created Haskell language?", "David Turner", "Philip Wadler", "Grace Hopper", "Bjarne Stroustrup", 2],
    # 20
    ["Who created HTML?", "John McCarthy", "Claude Shannon", "Tim Berners-Lee", "Dennis Ritchie", 3],
    # 21
    ["Who created CSS?", "James Gosling", "Tim Berners-Lee", "Linus Torvalds", "Håkon Wium Lie", 4],
]





# Prize levels for each question
level = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 20000000, 30000000, 50000000, 70000000]

try:
    # Main quiz loop for Beginner level
    for i in range(0, len(questions)):
        question = questions[i]
        print(f"\n\nQuestion for rupees {level[i]}")
        print(f"{question[0]}")
        print(f"a. {question[1]}   b. {question[2]}")
        print(f"c. {question[3]}   d. {question[4]}")

        # Get player's answer
        answer = int(input("Enter your answer(1-4) or 0 to quit: "))

        if answer == 0:  # Player chooses to quit
            print(f"Your winning amount is {level[i - 1] if i > 0 else 0}")
            break

        if answer == question[-1]:  # Correct answer
            print(f"Your answer is correct. Winning amount is: {level[i]}")
        else:  # Incorrect answer
            print(f"Your answer is wrong. The correct answer is option {question[-1]}")
            print(f"Your winning amount is {level[i - 1] if i > 0 else 0}")
            break

except ValueError:
    print("Invalid input! Please enter a number between 0 and 4.")

# Intermediate level
level_2 = int(input("Do you want to go for Intermediate level questions? (0 for No, 1 for Yes): "))

if level_2 == 1:
    questions_2 = [
         # 1
            ["Which data structure follows the First In First Out (FIFO) principle?",
            "Stack", "Queue", "Array", "Linked List", 2],

            # 2
            ["What is the time complexity of binary search in a sorted array?",
            "O(n)", "O(log n)", "O(n^2)", "O(n log n)", 2],

            # 3
            ["Which sorting algorithm has the worst-case time complexity of O(n^2)?",
            "Merge Sort", "Quick Sort", "Bubble Sort", "Heap Sort", 3],

            # 4
            ["What is the output of the expression 3 + 2 * 2 in Python?",
            "10", "7", "9", "12", 2],

            # 5
            ["Which of the following is not a built-in data type in Python?",
            "Tuple", "Set", "Dictionary", "Queue", 4],

            # 6
            ["What keyword is used to define a function in Python?",
            "define", "function", "def", "func", 3],

            # 7
            ["In object-oriented programming, what concept allows the same function to perform differently based on the object?",
            "Inheritance", "Encapsulation", "Polymorphism", "Abstraction", 3],

            # 8
            ["Which of these is a mutable data structure in Python?",
            "Tuple", "String", "List", "Set", 3],

            # 9
            ["Which method is used to add an element to the end of a list in Python?",
            "insert()", "append()", "push()", "add()", 2],

            # 10
            ["What will be the output of the following code snippet?\n\nx = 10\ny = 20\nx, y = y, x\nprint(x, y)",
            "10 20", "20 10", "Error", "None", 2]
       
    ]

    # Intermediate level questions and prize amounts
    level_2_prizes = [320000, 640000, 1250000, 2500000, 5000000, 10000000, 20000000, 30000000, 50000000, 70000000]
    try:
        # Loop through Intermediate level questions
        for j in range(0, len(questions_2)):
            question_2 = questions_2[j]
            print(f"\n\nQuestion for rupees {level_2_prizes[j]}")
            print(f"{question_2[0]}")
            print(f"a. {question_2[1]}   b. {question_2[2]}")
            print(f"c. {question_2[3]}   d. {question_2[4]}")

            answer = int(input("Enter your answer(1-4) or 0 to quit: "))

            if answer == 0:  # Player chooses to quit
                print(f"Your winning amount is {level_2_prizes[j - 1] if j > 0 else 0}")
                break

            if answer == question_2[-1]:  # Correct answer
                print(f"Your answer is correct. Winning amount is: {level_2_prizes[j]}")
            else:  # Incorrect answer
                print(f"Your answer is wrong. The correct answer is option {question_2[-1]}")
                print(f"Your winning amount is {level_2_prizes[j - 1] if j > 0 else 0}")
                break

    except ValueError:
        print("Invalid input! Please enter a number between 0 and 4.")

else:
    print("Game Ends")

# Expert level
level_3 = int(input("Do you want to go for Expert level questions? (0 for No, 1 for Yes): "))

if level_3 == 1:
    questions_3 = [
      # 1
            ["What is the time complexity of searching for an element in a balanced B-tree with 'n' elements and maximum degree 'm'?",
            "O(log n)", "O(log m)", "O(log_m n)", "O(m log n)", 3],

            # 2
            ["In concurrent programming, which concept is used to prevent race conditions and ensure proper access to shared resources?",
            "Semaphore", "Deadlock", "Mutex", "Garbage Collection", 3],

            # 3
            ["In a red-black tree, which of the following is NOT a property that ensures the tree remains balanced?",
            "Every node is either red or black", 
            "The root is always black", 
            "Every red node must have exactly two black children", 
            "Every path from a node to its descendant NULL nodes has the same number of black nodes", 3],

            # 4
            ["Which algorithm is known to solve the all-pairs shortest path problem in O(n^3) time complexity?",
            "Dijkstra's Algorithm", "Kruskal's Algorithm", "Bellman-Ford Algorithm", "Floyd-Warshall Algorithm", 4],

            # 5
            ["What is the primary advantage of using a TRIE (prefix tree) over a hash table for managing a dynamic set of strings?",
            "Faster average insertion time", 
            "Less memory usage", 
            "Ability to search for words with shared prefixes efficiently", 
            "Higher space efficiency in all cases", 3]
        ]
    

    # Expert level questions and prize amounts
    level_3_prizes = [10000000, 20000000, 30000000, 50000000, 70000000]

    try:
        # Loop through Expert level questions
        for k in range(0, len(questions_3)):
            question_3 = questions_3[k]
            print(f"\n\nQuestion for rupees {level_3_prizes[k]}")
            print(f"{question_3[0]}")
            print(f"a. {question_3[1]}   b. {question_3[2]}")
            print(f"c. {question_3[3]}   d. {question_3[4]}")

            answer = int(input("Enter your answer(1-4) or 0 to quit: "))

            if answer == 0:  # Player chooses to quit
                print(f"Your winning amount is {level_3_prizes[k - 1] if k > 0 else 0}")
                break

            if answer == question_3[-1]:  # Correct answer
                print(f"Your answer is correct. Winning amount is: {level_3_prizes[k]}")
            else:  # Incorrect answer
                print(f"Your answer is wrong. The correct answer is option {question_3[-1]}")
                print(f"Your winning amount is {level_3_prizes[k - 1] if k > 0 else 0}")
                break

    except ValueError:
        print("Invalid input! Please enter a number between 0 and 4.")

else:
    print("Game ends")
