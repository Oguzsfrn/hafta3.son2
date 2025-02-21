import random

def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    
    if operation == '/':
        num1 = num1 * num2  
    
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def ask_to_continue():
    response = input("Devam etmek istiyor musunuz? (E/H): ").strip().lower()
    return response == 'e'

def main():
    while True:
        question, answer = generate_question()
        print(f"Soru: {question}")
        user_answer = float(input("Cevabınız: "))
        
        if user_answer == answer:
            print("Doğru!")
        else:
            print(f"Yanlış! Doğru cevap: {answer}")
        
        if not ask_to_continue():
            break

if __name__ == "__main__":
    main()
