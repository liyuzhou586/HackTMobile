import { Component, OnInit } from '@angular/core';
import {BackendService} from '../services/backend.service';
import {Subject} from 'rxjs';

@Component({
  selector: 'app-phone',
  templateUrl: './phone.component.html',
  styleUrls: ['./phone.component.scss']
})
export class PhoneComponent implements OnInit {
  public stuff;
  public phone;
  private _unsubscribe = new Subject<any>();
  constructor(private backendService: BackendService) { }

  ngOnInit() {
  }

  phoneRecommendation(){
    this.backendService.deviceRec().subscribe(data => {
      this.phone = data;
    });
  }

  displayMembers() {
    this.backendService.aboutUs().subscribe(rs => {
      this.stuff = rs;
    })
  }

}
