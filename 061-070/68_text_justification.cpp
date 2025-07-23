
/*
68. Text Justification (https://leetcode.com/problems/text-justification/description/?envType=study-plan-v2&envId=top-interview-150)

loop over each word in words, summing up the total length of the current line without padding
    add each word into currLine vector
        for each word added that is not the last word, add a space to the end of each word

    make sure to include spaces too!
    every time you add a new word on top of the first word, add a space to the end of the word
        then add the length of the string to the total length of line, including the added space

    each word's length is guaranteed to be greater than 0 and not exceed maxWidth
        this means we can just initialize currLine with the first word immediately
            if the first word's length == maxWidth, i'm pretty sure the extra space will be removed, since first word is the last word

if the total length of the current line without padding exceeds the maxWidth, remove the last word
    or just check that the last word doesn't exceed the maxWidth before adding

now you have a list of words that make up a line of text in the result
    need to divide spaces evenly, with empty slots on the left being assigned more spaces than slots on the right
we have the current length of the line of text with a single space between each word
    while the current length of the line is less than maxWidth, add a space after each word from left to right (excluding the last word)
        stop when current length == maxWidth

repeat the process of adding words to vector currLine, keep track of the total length of the line
    when you reach the end of words, currLine is the last line
        just don't pad the last line and left justify it and it "should" be simple

runtime: O(n * maxWidth) where n is the length of words
space: O(n)

lmao this beats like 0.3% of people probably because theres a O(n) solution
*/

#include <iostream>
#include <vector>
using namespace std;

vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> currLine;
    vector<string> res;

    // adding words of the current line
    int i = 0;
    int lineNumber = 1;
    while (i < words.size()) {
        currLine = {words[i] + " "};
        int lineLength = words[i].length() + 1; // including the space

        // cout << "--------- LINE " << to_string(lineNumber) << " ---------" << endl;
        // cout << "CURRENT LINE INITIALIZED WITH " << words[i] << endl;
        // cout << "CURRENT LENGTH " << lineLength << endl;

        i++;

        while (i < words.size()) {
            string currWord = words[i];

            if (lineLength + currWord.length() > maxWidth) { // if adding the next word exceeds maxWidth, stop building currLine
                break;
            }

            currWord += " ";
            currLine.push_back(currWord);
            lineLength += currWord.length();
            i++;

            // cout << "ADDED " << currWord << endl;
            // cout << "CURRENT LENGTH " << lineLength << endl << endl;
        }

        // remove the space from the last word
        currLine[currLine.size()-1].pop_back();
        lineLength--;

        // keep adding spaces to ends of each word from left to right excluding the last word
        // keep doing this until the length of the line becomes maxWidth
        // edge case where there is only one word in the current line, since we exclude the last word
        if (i != words.size()) { // we do not pad or center the last line
            if (currLine.size() == 1) {
                currLine[0] += string(maxWidth-lineLength, ' ');
            } else {
                while (lineLength < maxWidth) {
                    int j = 0;
                    while (j < currLine.size()-1 && lineLength < maxWidth) {
                        currLine[j] += " ";
                        lineLength++;
                        j++;
                    }

                }
            }
        }   

        // concatenate all words in currLine to put into the result
        string line = "";
        for (string word : currLine) {
            line += word;
        }
        if (i == words.size()) {
            line += string(maxWidth-lineLength, ' ');
        }
        res.push_back(line);

        // for (string word : currLine) {
        //     cout << word;
        // }
        // cout << endl << endl;   
        // lineNumber++;
    }

    return res;
}

int main() {

    vector<string> words = {"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"};
    int maxWidth = 20;
    vector<string> res = fullJustify(words, maxWidth);

    for (string line : res) {
        cout << "|" << line << "|" << endl;
    }

    return 0;
}

/*
68. Text Justification (https://leetcode.com/problems/text-justification/description/?envType=study-plan-v2&envId=top-interview-150)

loop over each word in words, summing up the total length of the current line without padding
    add each word into currLine vector
        for each word added that is not the last word, add a space to the end of each word

    make sure to include spaces too!
    every time you add a new word on top of the first word, add a space to the end of the word
        then add the length of the string to the total length of line, including the added space

    each word's length is guaranteed to be greater than 0 and not exceed maxWidth
        this means we can just initialize currLine with the first word immediately
            if the first word's length == maxWidth, i'm pretty sure the extra space will be removed, since first word is the last word

if the total length of the current line without padding exceeds the maxWidth, remove the last word
    or just check that the last word doesn't exceed the maxWidth before adding

now you have a list of words that make up a line of text in the result
    need to divide spaces evenly, with empty slots on the left being assigned more spaces than slots on the right
we have the current length of the line of text with a single space between each word
    while the current length of the line is less than maxWidth, add a space after each word from left to right (excluding the last word)
        stop when current length == maxWidth

repeat the process of adding words to vector currLine, keep track of the total length of the line
    when you reach the end of words, currLine is the last line
        just don't pad the last line and left justify it and it "should" be simple

runtime: O(n * maxWidth) where n is the length of words
space: O(n)
*/

#include <iostream>
#include <vector>
using namespace std;

vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> currLine;
    vector<string> res;

    // adding words of the current line
    int i = 0;
    int lineNumber = 1;
    while (i < words.size()) {
        currLine = {words[i] + " "};
        int lineLength = words[i].length() + 1; // including the space

        // cout << "--------- LINE " << to_string(lineNumber) << " ---------" << endl;
        // cout << "CURRENT LINE INITIALIZED WITH " << words[i] << endl;
        // cout << "CURRENT LENGTH " << lineLength << endl;

        i++;

        while (i < words.size()) {
            string currWord = words[i];

            if (lineLength + currWord.length() > maxWidth) { // if adding the next word exceeds maxWidth, stop building currLine
                break;
            }

            currWord += " ";
            currLine.push_back(currWord);
            lineLength += currWord.length();
            i++;

            // cout << "ADDED " << currWord << endl;
            // cout << "CURRENT LENGTH " << lineLength << endl << endl;
        }

        // remove the space from the last word
        currLine[currLine.size()-1].pop_back();
        lineLength--;

        // keep adding spaces to ends of each word from left to right excluding the last word
        // keep doing this until the length of the line becomes maxWidth
        // edge case where there is only one word in the current line, since we exclude the last word
        if (i != words.size()) { // we do not pad or center the last line
            if (currLine.size() == 1) {
                currLine[0] += string(maxWidth-lineLength, ' ');
            } else {
                while (lineLength < maxWidth) {
                    int j = 0;
                    while (j < currLine.size()-1 && lineLength < maxWidth) {
                        currLine[j] += " ";
                        lineLength++;
                        j++;
                    }

                }
            }
        }   

        // concatenate all words in currLine to put into the result
        string line = "";
        for (string word : currLine) {
            line += word;
        }
        if (i == words.size()) {
            line += string(maxWidth-lineLength, ' ');
        }
        res.push_back(line);

        // for (string word : currLine) {
        //     cout << word;
        // }
        // cout << endl << endl;   
        // lineNumber++;
    }

    return res;
}

int main() {

    vector<string> words = {"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"};
    int maxWidth = 20;
    vector<string> res = fullJustify(words, maxWidth);

    for (string line : res) {
        cout << "|" << line << "|" << endl;
    }

    return 0;
}