// call_num_soundfile_Java_AI

import processing.sound.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;


HashMap<String, SoundFile> sounds;

ArrayList<String> wordlist;

PFont font;

Random random;


void setup() {

  size(500,300);

  textSize(20);

  background(234,216,92);


  sounds = new HashMap<String, SoundFile>();

  wordlist = new ArrayList<String>();

  random = new Random();


  font = createFont("PingFang TC",20);
  textFont(font);


  // 載入語音

  sounds.put("請",
    new SoundFile(this,"請.mp3"));

  sounds.put("號到",
    new SoundFile(this,"號到.mp3"));

  sounds.put("號櫃檯",
    new SoundFile(this,"號櫃檯.mp3"));


  // 0~9 數字語音

  for(int i=0;i<10;i++){

    sounds.put(
      str(i),
      new SoundFile(this, i+".mp3")
    );

  }

}



void draw(){

  background(234,216,92);


  // 紅色按鈕

  fill(255,0,0);

  rect(450,150,50,50);



  fill(0);


  // 顯示叫號紀錄

  for(int i=0;i<wordlist.size();i++){

    text(
      wordlist.get(i),
      40,
      i*30+30
    );

  }

}



// 播放語音

void speak(int num,int counter){


  sounds.get("請").play();

  delay(500);



  // 播放號碼

  String number=str(num);


  for(int i=0;i<number.length();i++){

    String d=str(number.charAt(i));


    sounds.get(d).play();

    delay(350);

  }



  sounds.get("號到").play();

  delay(500);



  // 播放櫃檯

  sounds.get(str(counter)).play();

  delay(350);



  sounds.get("號櫃檯").play();

}



// 滑鼠按下

void mousePressed(){


  if(mouseX>=450 &&
     mouseX<=500 &&
     mouseY>=150 &&
     mouseY<=200){



    int num=random.nextInt(9000)+1000;


    int p=random.nextInt(9)+1;



    String newText =
      "請"+num+"號到"+p+"號櫃檯";



    wordlist.add(newText);



    speak(num,p);

  }

}
