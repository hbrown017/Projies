/*
Name: Harry Brown III, 
Date: 3/1/15
Program: Car Inventory System
*/

import java.io.*;
import java.util.Scanner;

public class Inventory
{
	Car [] carray;
	int num_cars;
	int index = 0;
	int s = 0;
	int counter = 0;
	Inventory(int size)
	{
		num_cars=0;
		s = size;
		carray = new Car[size];
		carray = read_DB();
	}
	public Car[] read_DB()
	{
		File f = new File("DB.txt");
		Scanner fin = null;
		try
		{
			fin = new Scanner(f);
		} catch (FileNotFoundException e)
		{
			e.printStackTrace();
		}
		if(f.exists())
		{
			int nr=0; // number of row
			while (fin.hasNextLine()) //creates the array
			{
				String[] tokens = fin.nextLine().split("/");
				carray[nr]= new Car();
				carray[nr].brand = tokens[0];
				carray[nr].model = tokens[1];
				carray[nr].ID = Integer.parseInt(tokens[2]);
				carray[nr].year = Integer.parseInt(tokens[3]);
				carray[nr].mileage = Integer.parseInt(tokens[4]);
				carray[nr].price = Integer.parseInt(tokens[5]);
				nr++;
			}
			num_cars=nr;
		}
		else
		{
			System.out.println("Database was not found.");
		}
		fin.close();
		return carray;
	}
	public void add(Scanner in, int n) //adds cars to array
	{
		carray[num_cars] = new Car();

		if(n != 0) //update car information
		{
			num_cars = n;
			System.out.println("Please enter new up dates for this vehicle.");
		}

    	System.out.print("Brand: ");   carray[num_cars].set_brand(in.next());
    	System.out.print("Model: ");   carray[num_cars].set_model(in.next());
		System.out.print("ID: ");	   carray[num_cars].set_id(in.nextInt());
    	System.out.print("Year: ");    carray[num_cars].set_year(in.nextInt());
    	System.out.print("Mileage: "); carray[num_cars].set_mileage(in.nextInt());
    	System.out.print("Price: ");   carray[num_cars].set_price(in.nextInt());
		System.out.println();
    	num_cars++;
	}
	public void delete_car(String c)
	{
		while(index < s)
		{
			if(carray[index] != null && c.equals(carray[index].brand) 
				|| c.equals(carray[index].model))
			{
				carray[index].set_brand("\0");
				carray[index].set_model("\0");
				carray[index].set_id(0);
				carray[index].set_year(0);
				carray[index].set_mileage(0);
				carray[index].set_price(0);
				updateDB();
				System.out.println("The car is deleted. Thank you.");
				System.out.println();
				break;
			}
			index++;
		}
	}

	int update_car()
	{
		int x = 0;
		Scanner in = new Scanner(System.in);
		String b, m;
		System.out.println("What vehicle do you want to update?");
		System.out.print("Brand: "); b = in.next();
		System.out.print("Model: "); m = in.next();

		for(int i=0;i<num_cars;i++)
		{
			if(b.equals(carray[i].brand) && m.equals(carray[i].model))
			{
				x = i;
				break;
			}
		}
		return x;
	}

	/*public void sort_price()
	{
		insertionSort();
	}
	public void insertionSort()
	{       
		int i = 0;
		int key; 
		
		for(int x=1; x<s; x++)
		{
			key = carray[x].price;
			for(i=x-1; (i>=0)&&(carray[i].price<key); i--)
				carray[i+1].price = carray[i].price;
			
			carray[i+1].price = key;
		}
	}*/

	public void display() //display cars in array
	{
		if(carray[counter]== null)
		{
			System.out.println("Inventory is empty. Please add a car.");
			System.out.println();
		}
		else //display
		{
			System.out.println("Brand:\tModel:\tID:\tYear:\tMileage:\tPrice:");
			for(int i=0;i<num_cars;i++)
				System.out.println(carray[i].brand+"\t"+carray[i].model+"\t"+carray[i].ID+"\t"+carray[i].year+"\t"+carray[i].mileage+"\t\t"+carray[i].price);
			System.out.println();
		}
	}
	public void updateDB()
	{
		PrintWriter pw;
		try
		{
			pw = new PrintWriter("DB.txt");
			for(int i=0;i<num_cars;i++)
			{
				pw.println(carray[i].brand+"/"+carray[i].model+"/"+carray[i].ID+"/"+carray[i].year+"/"+carray[i].mileage+"/"+carray[i].price);
			}
			pw.close();
		} catch (FileNotFoundException e)
		{
			e.printStackTrace();
		}
	}
}
