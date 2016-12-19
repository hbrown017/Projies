/*
Name: Harry Brown III, 
Date: 3/1/15
Program: Car Inventory System
*/

import java.util.Scanner;

public class Carmax
{
	Carmax()
	{
		start();
	}
	public void start()
	{
		Scanner in = new Scanner(System.in);
		Inventory inv = new Inventory(100); //create inventory class object
		Menu m1 = new Menu(); // create menu class object
		while(true)
		{
			m1.menu_Main();
			m1.getUserInput(in);
			if (m1.c1=='1') // Add a car
			{
				inv.add(in, 0);
				inv.updateDB(); //add to DB file
			}
			else if (m1.c1=='2')
			{
				System.out.print("Enter car brand or model: ");
				String c = in.next();
				inv.delete_car(c); 
			}
			else if (m1.c1=='3')
			{
				inv.add(in, inv.update_car());
				inv.updateDB();
			}
			else if (m1.c1=='4')
			{
				inv.display();
			}
			else if (m1.c1=='5')
			{
				System.out.println("Sorry, option not ready.");
				//inv.sort_price();
			}
			else if(m1.c1=='6')
			{
				break;
			}
		}
		in.close();
	}
}
