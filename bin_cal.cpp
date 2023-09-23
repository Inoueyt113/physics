#include <iostream>
using namespace std;

#include <bitset>

string binaryToDecimal(const string &binaryNum)
{
    int decimalNum = 0;
    int base = 1;

    for (int i = binaryNum.length() - 1; i >= 0; i--)
    {
        if (binaryNum[i] == '1')
        {
            decimalNum += base;
        }
        base *= 2;
    }

    return to_string(decimalNum);
}

string decimalToBinary(const string &decimalNum)
{
    int num = stoi(decimalNum); // stringをintに変換
    string binaryStr = "";

    if (num == 0)
    {
        return "0";
    }

    while (num > 0)
    {
        int remainder = num % 2;
        binaryStr = to_string(remainder) + binaryStr;
        num /= 2;
    }

    return binaryStr;
}

// 1の補数を求める関数
string onesComplement(const string &binaryNum)
{
    string result = binaryNum;

    for (char &bit : result)
    {
        if (bit == '0')
        {
            bit = '1';
        }
        else if (bit == '1')
        {
            bit = '0';
        }
    }

    return result;
}

// 和を論理演算によって計算する関数
string binaryAddition(string a, string b, bool isDif)
{
    int maxLen = max(a.length(), b.length());
    while (a.length() < maxLen)
        a = '0' + a;
    while (b.length() < maxLen)
        b = '0' + b;

    int carry = 0;
    string result = "";

    for (int i = maxLen - 1; i >= 0; i--)
    {
        // 文字->0,1に変換
        int bitA = a[i] - '0';
        int bitB = b[i] - '0';

        int total = bitA + bitB + carry;
        int resultBit = total % 2;
        carry = total / 2;
        result = char(resultBit + '0') + result;
    }

    // オーバーフローが発生した場合、先頭に1を追加
    if (carry != 0 && !isDif)
    {
        result = '1' + result;
    }

    return result;
}

// 2の補数と和によって差を計算する関数
string binaryDifference(string a, string b)
{
    bool isNegative = false;
    if (stoi(binaryToDecimal(b)) > stoi(binaryToDecimal(a)))
    {
        string tmp = a;
        a = b;
        b = tmp;
        isNegative = true;
    }

    int maxLen = max(a.length(), b.length());
    while (a.length() < maxLen)
        a = '0' + a;
    while (b.length() < maxLen)
        b = '0' + b;

    string OnesComplement = onesComplement(b);
    string twosComplement = binaryAddition(OnesComplement, "1", true);
    string result = "";
    result = binaryAddition(a, twosComplement, true);

    if (isNegative)
        result = '-' + result;

    return result;
}

string binaryLeftShift(string binaryNum, int i)
{
    string result = "";
    for (int k = 0; k < i; k++)
        result = result + '0';

    result = binaryNum + result;
    return result;
}

string binaryDivide(string a, string b)
{
    int maxLen = max(a.length(), b.length());

    string result(maxLen, '0'); // resultを長さmaxLenの'0'で初期化
    string next = a;

    cout << b + "/";

    for (int i = 0; i < a.length() - b.length() + 1; i++)
    {
        cout << next << endl;                                          // iの範囲を修正
        string shiftNum = binaryLeftShift(b, maxLen - i - b.length()); // binaryLeftShiftの実装が必要
        cout << shiftNum << endl;

        if (stoi(binaryToDecimal(next)) >= stoi(binaryToDecimal(shiftNum)))
        {
            next = binaryDifference(next, shiftNum); // binaryDifferenceの実装が必要
            result[i] = '1';                         // resultに文字を設定
        }
        else
            cout << "-> 0" << endl;
    }
    result.pop_back();     // 最下位ビットを削除
    result = "0" + result; // 最上位ビットに0を挿入

    result.pop_back();     // 最下位ビットを削除
    result = "0" + result; // 最上位ビットに0を挿入

    return result;
}

int main()
{
    int decimalNum1, decimalNum2;
    cout << "decimalNum1>> ";
    cin >> decimalNum1;
    cout << "decimalNum2>> ";
    cin >> decimalNum2;
    string binaryNum1 = decimalToBinary(to_string(decimalNum1));
    string binaryNum2 = decimalToBinary(to_string(decimalNum2));

    string sum = binaryAddition(binaryNum1, binaryNum2, false);
    string dif = binaryDifference(binaryNum1, binaryNum2);
    string div = binaryDivide(binaryNum1, binaryNum2);

    cout << binaryNum1 << " + " << binaryNum2 << " = " << sum << endl;
    cout << binaryNum1 << " - " << binaryNum2 << " = " << dif << endl;
    cout << binaryNum1 << " / " << binaryNum2 << " = " << div << endl;

    cout << binaryToDecimal(binaryNum1) << " + " << binaryToDecimal(binaryNum2) << " = " << binaryToDecimal(sum) << endl;
    cout << binaryToDecimal(binaryNum1) << " - " << binaryToDecimal(binaryNum2) << " = " << binaryToDecimal(dif) << endl;
    cout << binaryToDecimal(binaryNum1) << " / " << binaryToDecimal(binaryNum2) << " = " << binaryToDecimal(div) << endl;

    return 0;
}