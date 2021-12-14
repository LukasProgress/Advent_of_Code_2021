import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

class Main{
    
    //extract data method
    public static ArrayList<String> getInput(){
        ArrayList<String> dataIn = new ArrayList<String>();
        try(BufferedReader br = new BufferedReader(new FileReader("Data.txt"))) {
            for(String line; (line = br.readLine()) != null; ) {
                dataIn.add(line);
            }
            return dataIn;
        } catch (Exception e)
        {
            System.err.println(e.getMessage()); // handle exception
            return null;
        }
    }

    //solve part 1
    public static void task1(ArrayList<String> data){
        ArrayList<String> results = new ArrayList<String>();
        for (String s : data){
            //Split the lines so the outputs are individual strings
            String[] split = s.split("\\|");
            String[] outputs = split[1].split(" ");
            //append the outputs to the result array:
            for (int i = 0; i < outputs.length; i++){
                results.add(outputs[i]);
            }
        }
        //After these loops, count the 1s, 4s, 7s, and 8s (strings with lengt 2, 4, 3 or 7)
        int count = 0;
        for (String s : results){
            int l = s.length();
            if (l == 2 || l == 3 || l == 4 || l == 7){
                count++;
            }
        }
        //print the result:
        System.out.println(count);
    }

    //solve task 2 (considerably harder, phew)
    public static void task2(ArrayList<String> data){
        int result = 0;
        for (String s : data){
            //Split the lines so the outputs are individual strings
            String[] split = s.split("\\|");
            String[] inputs = split[0].split(" ");
            String[] outputs = split[1].split(" ");
            
            //append the outputs to the result array:
            int fourDigitNumber = getNumber(inputs, outputs);

            result += fourDigitNumber;
        }
        System.out.println(result);
    }

    public static int getNumber(String[] inputs, String[] outputs){
        ArrayList<String> remainingInputs = new ArrayList<String>();
        for (String s : inputs){
            remainingInputs.add(s);
        }
        String[] numbers = new String[10];

        // assign 1, 7, 4 and 8
        for (String s : remainingInputs){
            switch (s.length()){
                case 2:
                numbers[1] = s;
                break;
                case 3:
                numbers[7] = s;
                break;
                case 4:
                numbers[4] = s;
                break;
                case 7:
                numbers[8] = s;
            }
        }
        
        remainingInputs.remove(numbers[1]);
        remainingInputs.remove(numbers[7]);
        remainingInputs.remove(numbers[4]);
        remainingInputs.remove(numbers[8]);
        //assign 9 and 3
        for (String s : remainingInputs){
            if (s.length() == 6 && isSubset(numbers[4], s)){
                numbers[9] = s;
            }
            if (s.length() == 5 && isSubset(numbers[7], s)){
                numbers[3] = s;
            }
        }
        remainingInputs.remove(numbers[9]);
        remainingInputs.remove(numbers[3]);
        //assign 5 and 2
        for (String s : remainingInputs){
            if (s.length() == 5 && isSubset(s, numbers[9])){
                numbers[5] = s;
            } else if (s.length() == 5){
                numbers[2] = s;
            }
        }
        remainingInputs.remove(numbers[5]);
        remainingInputs.remove(numbers[2]);
        //assign 0 and 6
        for (String s : remainingInputs){
            if (s.length() == 6 && isSubset(numbers[5], s)){
                numbers[6] = s;
            } else {
                numbers[0] = s;
            }
        }

        //Now calculate the solution:
        String result = "";
        for (String s : outputs){
            for (int i = 0; i < numbers.length; i ++){
                System.out.println("output: " + s + " number: " + i + " " + numbers[i]);
                if (isSubset(s, numbers[i]) && isSubset(numbers[i], s)){
                    System.out.println("SUCCESS!!!-----");
                    result += Integer.toString(i);
                }
            }
        }
        System.out.println(result);
        int solution = Integer.valueOf(result);


        return solution;
    }

    public static boolean isSubset(String is, String of){
        for (String s : is.split("|")){
            if (!of.contains(s)){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        ArrayList<String> data = getInput();
        //First, only care about the small numbers:
        task1(data);
        task2(data);
    }



}   
