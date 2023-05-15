def find_solutions(result_value = 200):
    digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    operators = ["+", "-", ""]

    def calcualte_expression(expression):
        result = 0
        operator = "+"
        number = ""

        for char in expression:
            if char.isdigit():
                number += char
            else:
                if operator == "+":
                    result += int(number)
                else:
                    result -= int(number)
                number = ""
                operator = char

        if operator == "+":
            result += int(number)
        else:
            result -= int(number)

        return result

    def create_expression(expression, index):

        if index == len(digits):
            if calcualte_expression(expression) == result_value:
                print(expression)
            return

        for operator in operators:
            new_expression = expression + operator + str(digits[index])
            create_expression(new_expression, index+1)

    create_expression("9", 1)

find_solutions()
