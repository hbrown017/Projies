/*
Name: Harry Brown III, 
Date: 3/1/15
Program: Car Inventory System
*/

import java.io.*;
public class mainCar
{
	public static void main(String[] args) throws IOException
	{
		File in = new File("DB.txt");
		if(!in.exists()) //create file if not found
		{
			PrintWriter p = new PrintWriter(in);
			p.close();
		}
		new Carmax();
	}

}
