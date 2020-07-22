const Discord = require('discord.js');
const asnycio = require('asyncio')
const client = new Discord.Client();
const token = process.env.token
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
if(message.content == 'embed') {
  let img = 'https://cdn.discordapp.com/icons/419671192857739264/6dccc22df4cb0051b50548627f36c09b.webp?size=256';
  let embed = new Discord.RichEmbed()
    .setTitle('타이틀')
    .setURL('http://www.naver.com')
    .setAuthor('나긋해', img, 'http://www.naver.com')
    .setThumbnail(img)
    .addBlankField()
    .addField('Inline field title', 'Some value here')
    .addField('Inline field title', 'Some value here', true)
    .addField('Inline field title', 'Some value here', true)
    .addField('Inline field title', 'Some value here', true)
    .addField('Inline field title', 'Some value here1\nSome value here2\nSome value here3\n')
    .addBlankField()
    .setTimestamp()
    .setFooter('나긋해')
}
client.login(token);