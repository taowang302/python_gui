# python_gui
## API for login:

  Method:POST
  
  {
  	"method":"login",
  	"information":{
		"name":string,
		"passwd":string
  	}
  }

Return:

{
    "status": status
    "information": data
}

Example:

{
	"method":"login",
	"information":{
		"name":"tom",
		"passwd":"123456"
	}
}

## API for BTC OP_RETURN

  Method:POST
  
  
 {
"method":"op_return"
"information":{
	"address":"string",
	"amount":"number"
	"metadata":"string"
	"if_testnet":"bool"
			  }
}

Return:

{
    "status": status,
    "information": data
}

Example:

{
"method":"op_return",
"information":{
	"address":"n3pmTQV9FqQoTmzEAnkfedXbNqwfmqxbbz",
	"amount":"0.00001",
	"metadata":"string",
	"if_testnet":"1"
			  }
}

## API for FactomTool

 Method:POST
 
 {
"method":"factom_action"
"information":{
	"command":command,
	"data":data
			  }
}

Return:

{
    "status": status,
    "information": data
}

Example:

{
"method":"factom_action",
"information":{
	"command":"factoid-balance",
	"data":{"address":"FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q"}
			  }
}
