import {Component, Input, OnInit} from '@angular/core';
import {Newspaper} from "../shared/Newspaper";

@Component({
  selector: 'hs-result-element',
  templateUrl: './result-element.component.html',
  styleUrls: ['result-element.component.css']
})
export class ResultElementComponent implements OnInit {

  @Input()
  newspaper: Newspaper;

  constructor() { }

  ngOnInit() {
  }

}
