public class Walk{
  
  HashMap<Character, Character> opposites;
  HashMap<Character, Character> rightTurn;
  
  int gridStep;
  private ArrayList<Character> stepChars;
  private ArrayList<PVector> stepVectors;
  PVector tail;
  PVector head;
  
  public Walk(Grid g){
    opposites = new HashMap();
    opposites.put('U','D');
    opposites.put('D','U');
    opposites.put('R','L');
    opposites.put('L','R');
    
    rightTurn = new HashMap();
    rightTurn.put('U','R');
    rightTurn.put('R','D');
    rightTurn.put('D','L');
    rightTurn.put('L','U');
    
    
    gridStep = g.gridStep;
    stepChars = new ArrayList();
    stepVectors = new ArrayList();
    head = g.center.copy();
    tail = head.copy();
    stepVectors.add(tail);
  }
  
  public Walk(String walkString, Grid g){
    opposites = new HashMap();
    opposites.put('U','D');
    opposites.put('D','U');
    opposites.put('R','L');
    opposites.put('L','R');
    
    rightTurn = new HashMap();
    rightTurn.put('U','R');
    rightTurn.put('R','D');
    rightTurn.put('D','L');
    rightTurn.put('L','U');
    
    
    gridStep = g.gridStep;
    stepChars = new ArrayList();
    stepVectors = new ArrayList();
    head = g.center.copy();
    tail = head.copy();
    stepVectors.add(tail);
    
    String translated = translate(walkString);
    for(int i = 0; i < translated.length(); i++){
      addStep(translated.charAt(i));
    }
  }
  
  public void addStep(char stepChar){
    // Step nStep = new Step(stepNum);
    switch(stepChar){
     case 'U':
       stepVectors.add(new PVector(tail.x, tail.y - gridStep));
       break;
     case 'D':
       stepVectors.add(new PVector(tail.x, tail.y + gridStep));
       break;
     case 'L':
       stepVectors.add(new PVector(tail.x - gridStep, tail.y));
       break;
     case 'R':
       stepVectors.add(new PVector(tail.x + gridStep, tail.y));
       break;
     default:
       return;
    }
    tail = stepVectors.get(stepVectors.size() - 1).copy();
    stepChars.add(stepChar);
  }
  
  public void display(){
    for(int i = 0; i < stepVectors.size() - 1; i++){
      PVector start = stepVectors.get(i).copy();
      PVector end = stepVectors.get(i + 1).copy();
      stroke(0);
      strokeWeight(5);
      line(start.x, start.y, end.x, end.y);
      strokeWeight(1);
    }
  }
  
  private String translate(String walkStr){
    
    if(walkStr == "")
      return "";
    if(walkStr == "2")
      return "R";
    String translated = "";
    int i = 0;
    while(i < walkStr.length()){
      if(walkStr.charAt(i) == '1'){ //<>//
        if(i == 0)
          translated += 'R';
        else
          translated += opposites.get(translated.charAt(i-1));
      }
      else if(walkStr.charAt(i) == '2'){
        translated += translated.charAt(i-1);
      }
      else if(walkStr.charAt(i) == '3'){
        if(i >= 2){
          if(walkStr.charAt(i-1) == '2')
            translated += rightTurn.get(translated.charAt(i-1));
          else
            translated += translated.charAt(i-2);
        }
        else{
          translated += rightTurn.get(translated.charAt(i-1));
        }
      }
      else if(walkStr.charAt(i) == '4'){
        translated += opposites.get(translated.charAt(i-2));  
      }
      i++;
    }
    return translated;
  }
  
}
