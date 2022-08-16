function this_is_a_test(){
  const spawner = require('child_process').spawn;

  // SEND STRING
  // const data_to_pass_in = 'Send this to python script';

  // SEND ARRAY
  // const data_to_pass_in = ['Send this to python script'];

  // SEND JSON
  const data_to_pass_in = {
    data_sent: 'User_name',
    data_returned: undefined
  };
  console.log('Data sent to python script: ', data_to_pass_in);
  // \website-files\\app.js

  const python_process = spawner('python', ['./website-files/python.py', JSON.stringify(data_to_pass_in)]);

  python_process.stdout.on('data', (data) => {
    console.log('Data recieved from python script: ', JSON.parse(data.toString()));
    // alert(JSON.parse(data.toString()));
  });
}
// Run == node website-files/javascript.js
