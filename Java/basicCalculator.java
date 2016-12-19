/*
Name: Harry Brown III
Program: Basic calculator
Decription: 
    Takes two user input values and adds, subtracts,
    multiplies, divides, and finds the modulus.
*/

package basicCalculator;
import java.util.Scanner;

public class BasicCalculator
{
	public static void main(String[] args) 
	{
            //create scanner object
            Scanner in = new Scanner(System.in);
            
            //declare variables
            int result = 0;
            int num1 = 0;
            int num2 = 0;
            
            //get user input
            System.out.print("Please input two integers: ");
            num1 = in.nextInt();
            num2 = in.nextInt();
            
            //perform calculations and display
            result = num1 + num2;
            System.out.println("Addition: "+result);

            result = num1 - num2;
            System.out.println("Subtraction: "+result);

            result = num1 / num2;
            System.out.println("Integer division: "+result);

            result = num1 % num2;
            System.out.println("Modulus: "+result);
		
	}
}
