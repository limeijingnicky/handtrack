class Main {
public static void main(String[] args) {

  int layers = 4;
        
  for(int layer =1; layer<=layers;layer++){
  
          int leng_l = (layers-layer) *1;
          for (int j = 0 ; j <leng_l ; j++){  
              System.out.print(" ");  
          }
          int leng = 1 + (layer-1) * 2;
          for (int j = 0 ; j <leng ; j++){
              System.out.print("*");  
          }
          // int leng_r = (layers-layer) * 1;
          // for (int j = 0 ; j <leng_r ; j++){
          //     System.out.print(" ");  
          // }
          System.out.println(""); 

  }
