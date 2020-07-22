const Discord = require('discord.js');
const asnycio = require('asyncio')
const client = new Discord.Client();
const token = process.env.token
client.on('ready', () => {
  console.log(`로그인: ${client.pings}`);
});
client.on('message', (message) => {
  if(message.content === '*핑') {
    message.channel.send(`pong ${client.ping}`);
  }
});
client.on('message', (message) => {
  if(message.content === '*주사위'){
    sans = Math.floor(Math.random() * 7);
  if(sans === 1) (
      message.channel.send(':game_die: 1')
  )
  if(sans === 2) (
    message.channel.send(':game_die: 2')
  )
  if(sans === 3) (
    message.channel.send(':game_die: 3')
  )
  if(sans === 4) (
      message.channel.send(':game_die: 4')
  )
  if(sans === 5) (
    message.channel.send(':game_die: 5')
  )
  if(sans === 6) (
    message.channel.send(':game_die: 6')
  )
  }
});
client.login(token);