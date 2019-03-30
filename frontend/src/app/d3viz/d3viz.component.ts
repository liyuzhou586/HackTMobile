import { Component, OnInit } from '@angular/core';
import * as d3 from "d3";

@Component({
  selector: 'app-d3viz',
  templateUrl: './d3viz.component.html',
  styleUrls: ['./d3viz.component.scss']
})
export class D3vizComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  clicked(event) {
    d3.select(event.target)
      .append('circle')
      .attr('cx', event.x)
      .attr('cy', event.y)
      .attr('r', 10)
      .attr('fill','red')
  }

}
