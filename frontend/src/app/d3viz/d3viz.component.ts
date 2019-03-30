import { Component, OnInit } from '@angular/core';
import * as d3 from "d3";
import { BackendService } from '../services/backend.service';

@Component({
  selector: 'app-d3viz',
  templateUrl: './d3viz.component.html',
  styleUrls: ['./d3viz.component.scss']
})
export class D3vizComponent implements OnInit {
  private queryRs;
  
  constructor(private backendService: BackendService) {
    this.backendService.queryRs$.subscribe(rs => {
      if(rs) {
        this.queryRs = rs;
      }
    });
  }

  ngOnInit() {
  }



  

}
