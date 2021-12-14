class Solution {
    public List<String> fizzBuzz(int n) {
        String array[]=new String[n]; 
        List<String> ls = new ArrayList<String>();
        for(int i=0; i< n; i++){
            if((i+1)%3==0 && (i+1)%5==0){
                array[i] = "FizzBuzz";
            }
            else if((i+1)%3==0){
                array[i] = "Fizz";
            }
            else if((i+1)%5==0){
                array[i] = "Buzz";
            }
            else{
                array[i] = String.valueOf(i+1);
            }
            ls = Arrays.asList(array);
            
        }
        return ls;
    }
}
            
    
