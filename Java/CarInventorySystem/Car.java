/*
Name: Harry Brown III, 
Date: 3/1/15
Program: Car Inventory System
*/

import java.util.Scanner;
public class Car
{
	Scanner in = new Scanner(System.in);
	String brand;
	String model;
	int ID;
	int year;
	int mileage;
	int price;

	//Set field methods
	public void set_brand(String b)
	{
		brand = b;
	}
	public void set_model(String m)
	{
		model = m;
	}
	public void set_id(int i)
	{
		ID = i;
	}
	public void set_year(int y)
	{
		year = y;
	}
	public void set_mileage(int m)
	{
		mileage = m;
	}
	public void set_price(int p)
	{
		price = p;
	}

	//Display methods
	public void disp_brand()
	{
		System.out.println(brand);
	}
	public void disp_model()
	{
		System.out.println(model);
	}
	public void disp_ID()
	{
		System.out.println(ID);
	}
	public void disp_year()
	{
		System.out.println(year);
	}
	public void disp_mileage()
	{
		System.out.println(mileage);
	}
	public void disp_price()
	{
		System.out.println(price);
	}

}
