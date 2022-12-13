data = {
	"daa9ce6e-749b-4d2b-8aaa-7cea524d04af": {
		"data": {
			"jid": 14,
			"devId": "3cebf247-4a2b-49b4-9c20-ade38c57b0da",
			"evt": {
				"etm": "2022-03-16T11:17:21Z",
				"csm": 0
			},
			"dev": "water_measure"
		},
		"meta": {
			"ver": "1.0",
			"gId": "20e64e2d-27a2-4471-b0a4-97d0c426c3e4"
		}
	},
	"72b68354-1f83-4c10-a322-db09724ec40b": {
		"data": {
			"jid": 9,
			"devId": "22ad83a2-75de-4238-be92-67ed773be318",
			"evt": {
				"etm": "2022-03-16T11:17:21Z",
				"csm": 0
			},
			"dev": "water_measure"
		},
		"meta": {
			"ver": "1.0",
			"gId": "20e64e2d-27a2-4471-b0a4-97d0c426c3e4"
		}
	},
 "72b68354-1f83-4c10-a322-db09724ec709": {
		"data": {
			"jid": 10,
			"devId": "22ad83a2-75de-4238-be92-67ed773betyu",
			"evt": {
				"etm": "2022-03-16T11:17:21Z",
				"csm": 0
			},
			"dev": "water_measure"
		},
		"meta": {
			"ver": "1.0",
			"gId": "20e64e2d-27a2-4471-b0a4-97d0c426c78"
		}
	}
 
}



for p_id, p_info in data.items():
    print("\nPerson ID:", p_id)
    
    print(data[p_id])
    
    # for key in p_info:
        # print(key + ':', p_info[key])