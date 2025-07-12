

/*
71. Simplify Path (https://leetcode.com/problems/simplify-path/description/)

feels like a stack problem
put all directories into a stack
when ".." is encountered, pop from the top of the stack

iterate through the input path
    a slash or multiple consecutive slashes denote a new directory
    treat three or more consecutive dots as a directory name
    ignore single dots??? i think since you are just moving to your current directory aka doing nothing
    string consecutive letters into directory anems and put them into the stack
    when ".." is encountered, pop from the top of the stack

runtime: O(n) where n is the length of path
space: O(n)

i hate this question so much
i wasn't locked in
wasted like two hours of my life
could've done this in twenty minutes
*/


#include <iostream>
#include <stack>
#include <vector>
using namespace std;

string getDirectory(string& s, int& i) {
    

    // if s[i] is literally anything else 
    // return the substring before the next '/' or end of string
    int start = i;
    while (i < s.size() && s[i] != '/') {
        i++;
    }

    return s.substr(start, i-start);
}


string simplifyPath(string path) {
    string res = "/";
    vector<string> directories;

    int i = 0;
    while (i < path.length()) {

        // skip ALL slashes
        if (path[i] == '/') { 
            while (i < path.size() && path[i] == '/') {
                i++;
            }
        }

        if (i >= path.length()) {
            break;
        }

        string curr = getDirectory(path, i);

        // ignore single dots
        if (curr == ".") {
            continue;
        }

        if (curr == "..") {
            if (!directories.empty()) {
                directories.pop_back();
            }
        } else {
            directories.push_back(curr);
        }
    }

    for (string dir : directories) {
        res += dir;
        res += "/";
    }
    res.pop_back(); // remove the last "/"

    return res.empty() ? "/" : res;
}


int main() {
    string path = "/a/./b/../../c/";
    cout << simplifyPath(path) << endl;
    return 0;
}