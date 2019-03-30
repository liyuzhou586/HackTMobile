import { Component, OnInit } from '@angular/core';
import { BackendService } from '../services/backend.service';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-phone',
  templateUrl: './phone.component.html',
  styleUrls: ['./phone.component.scss']
})
export class PhoneComponent implements OnInit {
  public stuff;
  public phone;
  public queryResult;
  private nextQueryBody;
  private _unsubscribe = new Subject<any>();
  constructor(private backendService: BackendService) { }

  ngOnInit() {
  }

  phoneRecommendation() {
    this.backendService.deviceRec().subscribe(data => {
      this.phone = data;
    });
  }

  displayMembers() {
    this.backendService.aboutUs().subscribe(rs => {
      this.stuff = rs;
    });
  }

  query() {
    const queryJson = { "queryParam": this.nextQueryBody };
    this.backendService.queryStuff(queryJson).subscribe(rs => {
      this.queryResult = rs;
    });
  }

  csvToJSON(csv) {

    let lines = csv.split("\n");

    let result = [];

    let headers = lines[0].split(",");

    for (let i = 1; i < lines.length; i++) {

      let obj = {};
      let currentline = lines[i].split(",");

      for (let j = 0; j < headers.length; j++) {
        obj[headers[j]] = currentline[j];
      }

      result.push(obj);
    }
    return JSON.stringify(result); //JSON
  }

  onFileChange(event) {
    let reader = new FileReader();
    if (event.target.files && event.target.files.length > 0) {
      let file = event.target.files[0];
      reader.readAsText(file);
      reader.onload = (e: any) => {
        let csv = e.target.result;
        const json = this.csvToJSON(csv);
        console.log(json)
        this.nextQueryBody = json;
      }
    }
  }

}
