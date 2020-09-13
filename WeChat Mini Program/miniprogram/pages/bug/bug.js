// miniprogram/pages/bug/bug.js
var util = require("./../../utils/utils.js")
var TIME = util.formatTime(new Date());
Page({
  data: {
    date: TIME,
    imgList: [],
    textareaAValue: '',
    picker: ['黑屏，无法显示', '小程序闪退', '设备无法连接','画面比例显示不正确'],
  },
  PickerChange(e) {
    console.log(e);
    this.setData({
      index: e.detail.value
    })
  },
  DateChange(e) {
    this.setData({
      date: e.detail.value
    })
  },
  ChooseImage() {
    wx.chooseImage({
      count: 4, //默认9
      sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album'], //从相册选择
      success: (res) => {
        if (this.data.imgList.length != 0) {
          this.setData({
            imgList: this.data.imgList.concat(res.tempFilePaths)
          })
        } else {
          this.setData({
            imgList: res.tempFilePaths
          })
        }
      }
    });
  },
  textareaAInput(e) {
    this.setData({
      textareaAValue: e.detail.value
    })
  },
  showModal(e) {
    wx.showModal({
      title: '是否提交',
      content: '点击确定来提交表单',
      success(res) {
        if (res.confirm) {
          wx.showToast({
            title: '提交成功',
            icon: 'success',
            duration: 2000
          })
        } else if (res.cancel) {

        }
      }
    })
  },
})