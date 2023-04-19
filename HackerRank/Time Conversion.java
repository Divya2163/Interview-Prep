/*Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s= '12:01:00PM'
Return '12:01:00'.
s= '12:01:00AM'
Return '00:01:00'.*/

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
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static String timeConversion(String s) {
    // Write your code here
    String hour = s.substring(0, 2);
    int hr = Integer.parseInt(hour);
    if(s.substring(8, 10).equals("AM")){
        if(hr==12){
            return "00"+s.substring(2, s.length()-2);
        }
        return s.substring(0, s.length()-2);
    }
    else{
        if(hr==12){
        hr+=0;
        }else{
            hr+=12;
        }
        hour = String.format("%02d", hr);
        String result = hour+s.substring(2, s.length()-2);
        return result;
    }  
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = Result.timeConversion(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
