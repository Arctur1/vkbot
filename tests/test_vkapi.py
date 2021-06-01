from vkapi import VkRequest


def test_get_userinfo():
    response = VkRequest().get_userinfo(1)
    assert response['response'][0]['first_name'] == "Павел"


