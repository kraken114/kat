for epoch in range(n_epochs):
    _n = len(train_dl)
    for ix, inputs in enumerate(train_dl):
        loss,mAP = train_batch_mAP(inputs, model, criterion,optimizer)
        pos = (epoch + (ix+1)/_n)
        log.record(pos, trn_loss=loss.item(), mAP_train=mAP, end='\r')
    _n = len(val_dl)
    for ix,inputs in enumerate(val_dl):
        loss, mAP_v = validate_batch_mAP(inputs, model, criterion)
        pos = (epoch + (ix+1)/_n)
        log.record(pos, val_loss=loss.item(), mAP_val=mAP_v, end='\r')
    log.report_avgs(epoch+1)
    scheduler_1.step()
log.plot_epochs(['mAP_train','mAP_val'])
log.plot_epochs(['trn_loss', 'val_loss'])
