//Harry Brown III, 2/8/15, Homework 2: Program 2
package rockpaperscissor;
import java.util.Scanner;
public class rockPaperScissor
{
    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        String type ="NULL";	//user choice
        String cType ="NULL";	//computer choice
        String winner = "NULL";
        String r = "Rock";
        String p = "Paper";
        String s = "Scissor";
        boolean check = true;

        System.out.println("Start Game");
        System.out.println("1. Rock");
        System.out.println("2. Paper");
        System.out.println("3. Scissor");
        System.out.print("What do you want to throw? ");

        //computers random number from 1 to 3
        int compRan = 1+(int)(Math.random()*3); 

        //get users choice
        while(check)
        {
            int option = in.nextInt();
                if(option == 1)
                {
                    type = r;
                    check = false;
                }
                else if(option == 2)
                {
                    type = p;
                    check = false;
                }
                else if(option == 3)
                {
                    type = s;
                    check = false;
                }
                else
                {
                    System.out.print("Please enter a 1, 2, or 3... ");
                    check = true;
                }
        }

        //get computers choice
        if(compRan == 1)
            cType = r;
        else if(compRan == 2)
            cType = p;
        else
            cType = s;

        //display user and computer choice
        System.out.println("Computer: "+cType);
        System.out.println("You: "+type);
        System.out.println("");

        //check winner
        if(type == p && cType == r)
                winner = "You";
        else if(type == r && cType == p)
                winner = "Computer";
        else if(type == s && cType == p)
                winner = "You";
        else if(type == p && cType == s)
                winner = "Computer";
        else if(type == r && cType == s)
                winner = "You";
        else if (type == s && cType == r)
                winner = "Computer";
        else //in the event of a tie
                winner = "NULL";

        //display winner
        if(winner == "You")
                System.out.println(winner+" win!!");
        else if(winner == "NULL")
                System.out.println("It was a tie!!");
        else
                System.out.println(winner+" won...");

    }
}
