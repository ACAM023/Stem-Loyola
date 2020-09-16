'''
 * Copyright: STEM Loyola
 * Date     : August 2019
 * ID       : 19.08-A1
 * Level    : 1 (Beginner)
 *
 * Task     : In a certain hospital, all birth certificates are tagged with
 *            unique numbers. You have been told that girls receive birth
 *            certificates with even numbers and boys receive the ones with
 *            odd numbers.
 *
 *            You need to create a program that when given a birth certificate
 *            number, it will print either "It's a Boy" or "It's a Girl" on the
 *            screen depending on whether the number is odd or even respectively.
 *
 * Solved By: <Alvin>
 *     Email: <sonalpha023@gmail.com>
 *     Form : <Alumni>
 *    Stream: <PCM>
'''

# print("Hello!")

number = int(input())

if number % 2 == 0:
    print("It's a Girl")
else:
    print("It's a Boy")