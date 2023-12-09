# рабочая для входов
def in_for_mAP_true(batch):
  lst_boxes=batch[1]
  lst_labels=batch[2]
  lst = list(zip(lst_labels,lst_boxes))
  ground_date=[]
  for i,_ in enumerate(lst):
    t=list(zip(_[0],_[1]))
    # print(t)
    lst_data =[]
    for k in t:
      f=[i,k[0]]
      f.extend(k[1])
      f.insert(2,float(1))
      lst_data.append([np.around(float(i),4) for i in f])
    ground_date.extend(lst_data)
  for i in ground_date:
    i[0] = int(i[0])
    i[1] = int(i[1])
  return ground_date

save_path = 'ДИПЛОМ_6_3_SSD(итог_с_mAP)_САМОЛЕТЫ.pth'
torch.save(model.state_dict(), save_path)
!du -hsc {save_path} # size of the model on disk
