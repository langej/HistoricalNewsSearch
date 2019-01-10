import {Component, Input, OnInit} from '@angular/core';
import {Newspaper} from "../shared/Newspaper";

@Component({
  selector: 'hs-result-element',
  templateUrl: './result-element.component.html',
  styles: []
})
export class ResultElementComponent implements OnInit {

  @Input()
  private newspaper: Newspaper;

  constructor() { }

  ngOnInit() {
  }

}
