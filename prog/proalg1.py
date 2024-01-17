#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def edit_dist_dp(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Заполняем d[][] снизу вверх
    for i in range(m + 1):
        for j in range(n + 1):

            # Если первая строка пуста - вставить все символы второй строки
            if i == 0:
                dp[i][j] = j

            # Если вторая строка пуста - удалить все символы первой строки
            elif j == 0:
                dp[i][j] = i

            # Если последние символы одинаковы, игнорируем последний и рекурсивно вызываем для оставшейся строки
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # Если последний символ отличается, рассматриваем все возможности и находим минимум
            else:
                dp[i][j] = 1 + min(dp[i][j-1],       
                                   dp[i-1][j],        
                                   dp[i-1][j-1])       

    return dp[m][n]

def edit_dist_bu(A, B):
    n = len(A)
    m = len(B)

    D = [[0 for x in range(m + 1)] for x in range(n + 1)]

   
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 0 if A[i - 1] == B[j - 1] else 1
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] +
                          1, D[i - 1][j - 1] + c)

    return D[n][m]

if __name__ == "__main__":
    str1 = input("Введите строку 1: ")
    str2 = input("Введите строку 2: ")
    result_dp = edit_dist_dp(str1, str2)
    print(f"Результат edit_dist_dp: {result_dp}")
    # Преобразование строк в списки для edit_dist_bu
    A = list(str1)
    B = list(str2)

    result_bu = edit_dist_bu(A, B)
    print(f"Результат edit_dist_bu: {result_bu}")