import requests
import json


def get_submission_by_displayID(displayID, limit):
    api_url = f"http://localhost:8081/api/submissions"
    params = {}
    params['limit'] = limit

    submissionsIDList = []
    try:
        response = requests.get(api_url, params=params)
        # 检查是否成功获取响应
        if response.status_code == 200:
            # 解析API响应的JSON数据
            api_data = response.json()

            # 在这里处理API数据，可以根据需要进行进一步的处理
            api_data = api_data.get("data", {}).get("results", [])

            for data in api_data:
                if (data['problem'] == displayID):
                    submissionsIDList.append(data['id'])
            return submissionsIDList

        else:
            print(f"API请求失败，状态码: {response.status_code}")
            # 进一步处理错误情况，例如记录错误信息或采取其他措施

    except requests.exceptions.RequestException as e:
        print(f"API请求发生异常: {e}")
        # 处理请求异常，例如连接超时等情况


submissionsIDList = get_submission_by_displayID("1-1", 10000)
print()
