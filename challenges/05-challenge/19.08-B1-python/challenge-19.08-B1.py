'''
 * Copyright: STEM Loyola
 * Date     : August 2019
 * ID       : 19.08-B1
 * Level    : 1 (Amateur)
 *
 * Task     : Your form two friend, Ali, is currently learning how to solve
 *            quadratic equations. Ali knows that you are learning programming
 *            and has asked you to create a program that he can use to check if
 *            his answers are correct. Both you and Ali know that a quadratic
 *            equation is of the form: a^2 + bx + c = 0 and the value of "a"
 *            cannot be zero. Ali needs the program to input the three numbers
 *            (a, b and c) and produce the solution to the equation i.e. the
 *            value(s) of x that makes the equation zero.
 *
 *            In general, the two values of x that solve the equation can be
 *            computed as shown in Figure 1.
 *
 *            Note: (1) When b^2 < 4ac, the equation does not have real
 *                      solutions and your program should just say
 *                      "No Real Solutions".
 *                  (2) If a = 0, your program should just say
 *                      "The value of 'a' cannot be zero".

 *
 * Solved By: <Alvin>
 *     Email: <sonalpha023@gmail.com>
 *     Form : <Alumni>
 *    Stream: <PCM>
'''

print("Input the values of a, b, and c for solving the Quadratic equation.")
a, b, c = map(float, input().split())

def quadratic(a, b, c):
    if a == 0:
        return "The value of 'a' cannot be zero"
    elif b**2 < (4 * a * c):
        return "No Real Solutions"
    elif b**2 == (4 * a * c):
        return -b / (2 * a)
    else:
        x1 = (-b + pow(b**2 - (4*a*c), 0.5)) / 2 * a
        x2 = (-b - pow(b**2 - (4*a*c), 0.5)) / 2 * a

        return x1, x2

print(quadratic(a, b, c))