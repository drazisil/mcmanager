const info = require('../package.json')
const { main } = require('../src')

require('yargs')
    .scriptName(info.name)
    .usage('$0 <cmd> [args]')
    .command(
        'hello [name]',
        'welcome ter yargs!',
        yargs => {
            yargs.positional('name', {
                type: 'string',
                default: 'Cambi',
                describe: 'the name to say hello to',
            })
        },
        function(argv) {
            console.log('hello', argv.name, 'welcome to yargs!')
        }
    )
    .help().argv

console.log('Hello, world')
