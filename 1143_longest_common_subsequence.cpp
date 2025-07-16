


/*
1143. Longest Common Subsequence (https://leetcode.com/problems/longest-common-subsequence/description/)

compare the first character of each string
if they are the same: return 1 + longestCommonSubsequence(text1[1:], text2[1:])
if they are different: return max(longestCommonSubsequence(text1[1:], text2), longestCommonSubsequence(text1, text2[1:]))
once one of the two strings becomes length 0, return

need a dp table to memoize results
dp table will memoize the state of (i, j)

DO NOT CREATE A NEW SUBSTRING AT EACH RECURSIVE CALL
    JUST USE TWO POINTERS

set index i for text1[0] and j for text2[0]

at each recursive call, check if text1[i] == text2[j]
    if true, increment both i and j and recurse into function

whether text1[i] == text2[j] is true or false, recurse into the the other two possibilities:
    1. increment i and recurse
    2. increment j and recurse

out of the above three recursive calls, take the maximum of each returned value
memoize the max into the state of dp[i][j]

runtime: O(n * m) where n is text1.length() and m is text2.length()
space: O(n * m)
*/

#include <iostream>
#include <vector>
using namespace std;

int helper(string& text1, string& text2, int i, int j, vector<vector<int>>& dp) {
    
    if (i == text1.length() || j == text2.length()) {
        return 0;
    }

    if (dp[i][j] != -1) {
        return dp[i][j];
    }

    int largest = 0;
    if (text1[i] == text2[j]) {
        largest = 1 + helper(text1, text2, i+1, j+1, dp);
    }
    largest =  max(largest, max(helper(text1, text2, i+1, j, dp), helper(text1, text2, i, j+1, dp)));

    dp[i][j] = largest;
    return dp[i][j];
}

int longestCommonSubsequence(string text1, string text2) {
    vector<vector<int>> dp(text1.length()+1, vector<int>(text2.length()+1, -1));
    return helper(text1, text2, 0, 0, dp);
}

// int main() {
//     string text1 = "fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny";
//     string text2 = "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan";
//     cout << longestCommonSubsequence(text1, text2) << endl;

//     return 0;   
// }