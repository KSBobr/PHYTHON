"""
https://leetcode.com/problem-list/string/
url:https://leetcode.com/problems/integer-to-english-words/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        number_names = [
            "Zero",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens_names = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        scale_factors = [1_000_000_000, 1_000_000, 1_000]
        result_words = ""

        for scale in scale_factors:
            quotient = num // scale
            num %= scale

            if quotient > 0:
                hundreds_part = quotient // 100
                remainder_part = quotient % 100

                if hundreds_part > 0:
                    result_words += f" {number_names[hundreds_part]} Hundred"

                if remainder_part > 0:
                    if remainder_part < 20:
                        result_words += f" {number_names[remainder_part]}"
                    else:
                        tens_part = remainder_part // 10
                        ones_part = remainder_part % 10

                        result_words += f" {tens_names[tens_part]}"
                        if ones_part > 0:
                            result_words += f" {number_names[ones_part]}"

                if scale == 1_000_000_000:
                    result_words += " Billion"
                elif scale == 1_000_000:
                    result_words += " Million"
                elif scale == 1_000:
                    result_words += " Thousand"

        if num > 0:
            hundreds_part = num // 100
            remainder_part = num % 100

            if hundreds_part > 0:
                result_words += f" {number_names[hundreds_part]} Hundred"

            if remainder_part > 0:
                if remainder_part < 20:
                    result_words += f" {number_names[remainder_part]}"
                else:
                    tens_part = remainder_part // 10
                    ones_part = remainder_part % 10

                    result_words += f" {tens_names[tens_part]}"
                    if ones_part > 0:
                        result_words += f" {number_names[ones_part]}"

        return result_words.strip()
