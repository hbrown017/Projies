/*
Name: Harry Brown III, 
Date: 3/1/15
Program: Car Inventory System
*/

import java.util.Scanner;

public class Menu
{
	public char c1;
    public void getUserInput(Scanner in)
    {
        System.out.print("Please choose an option: "); c1 = in.next().charAt(0);
    }
    public void menu_Main()
    {
		Menu m = new Menu();
		Scanner in = new Scanner(System.in);

		System.out.println("Carmax Management Program");
        System.out.println("1. Add a car");
        System.out.println("2. Delete a car");
        System.out.println("3. Update a car");
        System.out.println("4. Display cars");
        System.out.println("5. Display cars (sort by price)");
        System.out.println("6. Exit");
		
    }
}
