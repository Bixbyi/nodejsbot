const Discord = require('discord.js');
const asnycio = require('asyncio')
const client = new Discord.Client();
const token = 'NzI1NTgzMDU5NjU0NjcyNDE1.XxgjXA.iOsmiz8uVkZTlH-2i0x3xXtGWEM'
client.on('ready', () => {
  console.log(`로그인: ${client.pings}`);
});
client.on('message', (message) => {
  if(message.content === '`핑') {
    message.channel.send(`pong ${client.ping}`);
  }
});
client.on('message', (message) => {
  if(message.content === '`주사위'){
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
    message.channel.send(':game_die: 2')
  )
  if(sans === 6) (
    message.channel.send(':game_die: 3')
  )
  }
});
client.on('message', (message) => {
if(message.content == '`정보'){;
  let embed = new Discord.RichEmbed()
    .setTitle('정보')
    .setURL('http://www.naver.com')
    .setAuthor('나긋해', img, 'http://www.naver.com')
    .setThumbnail(message.author.avatar)
    .addBlankField()
    .addField('닉네임',message.author.username)
    .addField('아이디', message.author.id, true)
    .addBlankField()
    .setTimestamp()
    .setFooter()
    message.channel.send(embed)
}
});
client.login(token);