import java.util.*;
import java.util.ArrayList;
import java.util.Date;
import java.text.SimpleDateFormat;

public class IBHS {
    public static void main (String[] args){
    SimpleDateFormat dt = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
    SimpleDateFormat df = new SimpleDateFormat("dd");
    SimpleDateFormat mf = new SimpleDateFormat("MM");
	String _current_date = df.format(new Date());
	String _current_month = mf.format(new Date());
	String date = dt.format(new Date());
	int current_date = Integer.parseInt(_current_date);
	int current_month = Integer.parseInt(_current_month);
	System.out.println("today is:" + date + "\n");

    final int[] levels = {0, 1, 3, 7, 14, 29};

    int[] dates = {22, 23, 24, 25, 26, 27, 28};
    int[] list = {1, 2, 3, 4, 5, 6, 7};
    String[] list1 = {"one", "two", "three", "four", "five", "six", "seven"};
    int[] months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

	ArrayList reviews = new ArrayList();
	for(int i=0; i<list.length; i++){
	    int result = current_date - dates[i];
	    if (result > 0) {
		for(int j=0; j<levels.length; j++) {
		    if (result == levels[j]) {
			System.out.println("review lists are:"+list[i]);
		    }
		}
	    }
	   else {
	       result = months[current_month] - dates[i] + current_date;
	       for(int j=0; j<levels.length; j++) {
	           if (result == levels[j]) {
                   System.out.println("review lists are:"+list[i]);
	           }
	       }
	   }
	}
    }
}

