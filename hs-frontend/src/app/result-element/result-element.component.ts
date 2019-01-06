import { Component, OnInit, Input } from '@angular/core';
import { Result } from '../shared/Result';

@Component({
  selector: 'hs-result-element',
  templateUrl: './result-element.component.html',
  styleUrls: ['./result-element.component.css']
})
export class ResultElementComponent implements OnInit {

  @Input() result: Result;

  @Input() queryString: string;

  fullText = false;

  constructor() { }

  ngOnInit() {
  }

  toggleFullText() {
    this.fullText ? this.fullText = false : this.fullText = true;
  }

}
