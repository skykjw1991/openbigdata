j_data={
    "response":
    {
        "header":{
            "resultCode":"0000","resultMsg":"OK"
        },
        "body":{
            "items":{
                "item":[
                    {
                        "baseDate":20180503,"baseTime":"0930","category":"LGT","fcstDate":20180503,"fcstTime":1000,"fcstValue":0,"nx":89,"ny":91
                    },
                    {
                        "baseDate":20180503,"baseTime":"0930","category":"LGT","fcstDate":20180503,"fcstTime":1100,"fcstValue":0,"nx":89,"ny":91
                    },
                    {
                        "baseDate":20180503,"baseTime":"0930","category":"LGT","fcstDate":20180503,"fcstTime":1200,"fcstValue":0,"nx":89,"ny":91
                    },
                    {
                        "baseDate":20180503,"baseTime":"0930","category":"RN1","fcstDate":20180503,"fcstTime":1000,"fcstValue":0,"nx":89,"ny":91
                    },
                    {
                        "baseDate":20180503,"baseTime":"0930","category":"RN1","fcstDate":20180503,"fcstTime":1100,"fcstValue":0,"nx":89,"ny":91
                    }
                ]
            }
        }
    }
}

print(j_data["response"]['body']['items']['item'][3]['category'])
print(j_data["response"]['body']['items']['item'][1]['category'])

# for i in j_data["response"]['body']['items']['item'][3:]:
#     # for j in i:
#     #     i['category']=='RN1'
#     #     # print(j)
#         print(i)

for i in j_data["response"]['body']['items']['item']:
    for j in i:
        ['category']=="RN1"
        print(j)


