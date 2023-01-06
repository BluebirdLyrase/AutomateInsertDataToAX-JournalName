void insertNow()
{
    boolean     _hasDone;
    container validateContainer;
    MapEnumerator   validateMapEnum;
    startlengthyOperation();

    this.InputAsciiIO_read();

        if (mapContainer.elements()) {
            mapEnumContainer = mapContainer.getEnumerator();
            validateMapEnum = mapContainer.getEnumerator();
            validateMapEnum.moveNext();
            validateContainer = validateMapEnum.currentValue();
            if (
                this.ValidateAciiValue(conPeek(validateContainer,#CarRegistration), 10)
                && this.ValidateAciiValue(conPeek(validateContainer,#InsuranceCustomerName), 50)
                && this.ValidateAciiValue(conPeek(validateContainer,#InsuranceNo), 15)
            ) {

            while (this.next()) {
                this.createMaster(this.conCSV());
                _hasDone = true;
            }

            if (_hasDone) {
                this.numberSeq_Used();
            }

            this.messageSuccess();

        } else {
            info(strFmt('ไม่สามารถ Import ข้อมูลได้ โปรดตรวจสอบการตั้งค่าภาษาของเครื่อง PC'));
        }
        }


    endlengthyOperation();
}