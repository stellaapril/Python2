/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Week2;

/**
 *
 * @author cst
 */
public class password {
    
    
    public static int lengthMin;
    public static int lengthMax;
    public static String[] reqChar;
    public static boolean result;
    
    public static void mian(String[] args){
        setLength(5,8);
        String[] reqChar={"@","$"};
        setreqChar(reqChar);
        
        
    }
    
    public static void setLength(int min, int max){
        lengthMin = min;
        lengthMax=max;
    }//close mehtod
    
    public static void setreqChar(String[] s){
        reqChar = s;
    }//close method
    
    public static boolean checkPassword(String psswd){
        if(psswd.length()<lengthMin){
            result=false;
        }else if(psswd.length()<lengthMax){
            result=true;
        }
                    
                    
            
        }
        return result;
    }
        
    
    
}
