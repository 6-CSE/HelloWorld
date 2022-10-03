import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Dimensions, TouchableOpacity } from 'react-native';

const HEIGHT = Dimensions.get('window').height;

export default function App() {
  const [word, setWord] = React.useState('Hello World');
  const wordList = [
    'Hello World',
    'Bonjour le monde',
    'Hola Mundo',
    'Hallo Welt',
    'Ciao Mondo',
    'Hej Verden',
    'Olá Mundo',
    'Привет мир',
    '你好，世界',
    'こんにちは世界',
    'नमस्ते दुनिया',
    'ہیلو ورلڈ',
    'مرحبا بالعالم',
  ]
  return (
    <View style={styles.container}>
      <Text style={styles.text}>{word}</Text>
      <StatusBar hidden />
      <TouchableOpacity 
      style={styles.circledBtn} 
      onPress={() => setWord(wordList[Math.floor(Math.random() * wordList.length)])}
      activeOpacity={0.9}
      >
        <View>
          <Text style={styles.btnText}>Say</Text>
        </View>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'rgba(0, 44, 254,0.7)',
    alignItems: 'center',
    justifyContent: 'center',
    height: HEIGHT * 0.8,
    borderBottomRightRadius: 100,
    borderBottomLeftRadius: 100
  },
  text: {
    color: 'white',
    fontSize: 48,
  },
  circledBtn: {
    backgroundColor: '#FEE134',
    width: 100,
    height: 100,
    borderRadius: 50,
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    bottom: -50,
  },
  btnText: {
    color: 'black',
    fontSize: 18,
  }
});
