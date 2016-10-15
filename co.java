package ajaxdemo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.Map;

import org.json.*;

public class co {

    public static String main(String ean)   {
	 //  String ean = "4260107220015";
       String ProductJson = getProduct(ean);
     try{
        JSONObject objJSON= new JSONObject(ProductJson);
        System.out.println(objJSON);
        String categoriesStr = objJSON.getJSONObject("product").getString("categories");
        String[] categories= categoriesStr.split(",");
        int CO2 = getCO2(categories);
        System.out.println(CO2);
		return Integer.toString(CO2);
     }catch(Exception e){
    	 return "-1";
     }
    }
 
    public static int getCO2(String[] categories) {
        Map<String,Integer> map = new HashMap<String, Integer>();
        map.put("Cola", 500);
        map.put("Mate", 600);
        map.put("wasser", 10);
        //...

        for (String cat:categories) {
            Integer verbrauch = map.get(cat);;
            if(verbrauch!=null) {
                return verbrauch;

            }else {

            }
        }
        System.out.println("Kategorie nicht vorhanden!");
        return -1;
    }




    public static String getProduct(String ean) {
        String json = "";

        //API call
        try {
            String url = "http://world.openfoodfacts.org/api/v0/product/"+ ean+".json";
            // System.out.println(url);
            String result = readJsonFromUrl(url);
            //System.out.println(result);
            return result;
        } catch (IOException e) {
            e.printStackTrace();
        }

       return "{Error while loading url}";
    }

    private static String readAll(Reader rd) throws IOException {
        StringBuilder sb = new StringBuilder();
        int cp;
        while ((cp = rd.read()) != -1) {
            sb.append((char) cp);
        }
        return sb.toString();
    }

    public static String readJsonFromUrl(String url) throws IOException {
        InputStream is = new URL(url).openStream();
        try {
            BufferedReader rd = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));
            String jsonText = readAll(rd);
            // JSONObject json = new JSONObject(jsonText);
            return jsonText;
        } finally {
            is.close();
        }
    }
}
