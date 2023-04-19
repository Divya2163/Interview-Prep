/*Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example
arr= [1,1,0,-1,-1]
There are  elements, two positive, two negative and one zero. Their ratios are 2/5,2/5 and 1/5. Results are printed as:

0.400000
0.400000
0.200000*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
    // Write your code here
    double negcount = 0;
    double poscount = 0;
    double zercount = 0;
    double negratio, posratio, zeroratio;
    double ans1,ans2,ans3;
    int n = arr.size();
     for(Integer i:arr){  
     if(i==0)
            zercount++;
        else if(i>0)
            poscount++;
        else
            negcount++; 
    }  
    negratio=negcount/n;
    posratio=poscount/n;
    zeroratio=zercount/n;
    ans1 = Math.round(negratio*10000000) / 10000000.0;
    ans2 = Math.round(posratio*10000000) / 10000000.0;
    ans3 = Math.round(zeroratio*10000000) / 10000000.0;
    System.out.println(ans2);
    System.out.println(ans1);
    System.out.println(ans3);
    } 
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}


