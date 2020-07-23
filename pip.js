const Discord = require('discord.js');
const asnycio = require('asyncio');
const googletrans = require('googletrans');
const client = new Discord.Client();
const token = process.env.token
client.on('ready', () => {
  console.log(`로그인: ${client.pings}`);
});
client.on('message', (message) => {
  if(message.content === 'hb!핑') {
    message.channel.send(`현재 빅스비시의 풍속은 ${client.ping}ms 입니다`);
  }
});
client.on('message', (message) => {
  if(message.content === 'hb!주사위'){
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
client.on('message', (message) => {
  if(message === 'hb!업타임') {
    let embed = new Discord.RichEmbed()
    .setColor('#0099ff')
    .setAuthor()
    .addField('업타임',`${client.uptime} 초입니다`)
    .setTimestamp()
  message.channel.send(embed)
  }
});
client.on('message',(message) => {
  if(message === 'hb!번역') {
    translator = translator()
    msg = message.content[8]
    result = translator.translate(msg, dest='en')
  message.channel.send(result)
  }
});
client.login(token);